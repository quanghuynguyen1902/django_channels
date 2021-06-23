<template>
  <div>
    <CRow>
      <CCol md="12">
        <CCard>
          <CCardHeader>
            <div class="button-table">
              <CButton color="dark" size="sm" @click="openFilter = true">
                Filter
                <CIcon name="cil-filter" height="15"></CIcon>
              </CButton>
            </div>
            <CModal
              title="Options"
              :closeOnBackdrop="false"
              :show.sync="openFilter"
            >
              <filter-component></filter-component>
              <div slot="footer" class="w-100">
                <CButton
                  color="light"
                  class="ml-1 mr-1 float-right"
                  @click="openFilter = false"
                >
                  Cancel
                </CButton>
                <CButton
                  color="info"
                  class="ml-1 mr-1 float-right"
                  @click="filterFuntion"
                >
                  Apply
                </CButton>
              </div>
            </CModal>
          </CCardHeader>

          <CCardBody>
            <CDataTable
              :items="changeData"
              :fields="fields"
              :items-per-page="10"
              hover
              sorter
            >
              <template #request_method="{item}">
                <td>
                  <CBadge :color="getBadge(item.request_method)">
                    {{ item.request_method }}
                  </CBadge>
                </td>
              </template>
              <template #show_details="{item, index}">
                <td class="py-2">
                  <CButton
                    color="primary"
                    variant="outline"
                    square
                    size="sm"
                    @click="toggleDetails(item, index)"
                  >
                    {{ Boolean(item._toggled) ? "Hide" : "Show" }}
                  </CButton>
                </td>
              </template>
              <template #details="{item}">
                <CCollapse
                  :show="Boolean(item._toggled)"
                  :duration="collapseDuration"
                >
                  <detail-request :item="item"></detail-request>
                </CCollapse>
              </template>
            </CDataTable>
            <CPagination
              :activePage.sync="page"
              :pages="totalpage"
              size="sm"
              align="center"
              @update:activePage="getResultPage(page)"
            />
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  </div>
</template>

<script>
import FilterComponent from "@/components/FilterComponent";
import DetailRequest from "@/components/DetailRequest";
import Api from "@/constants/backendApi";
import { mapGetters } from "vuex";
import UserService from "../api/userService";
export default {
  name: "Dashboard",
  components: {
    FilterComponent,
    DetailRequest
  },
  mounted() {
    if (!this.currentUser) {
      this.$router.push("/login");
    }
    this.getData();
  },
  data() {
    return {
      openFilter: false,
      collapseDuration: 0,
      fields: [
        { key: "user_id" },
        { key: "url" },
        { key: "request_method" },
        { key: "status" },
        {
          key: "show_details",
          label: "Detail",
          _style: "width:1%",
          sorter: false,
          filter: false
        }
      ],
      data: [],
      page: 1,
      totalpage: 1
    };
  },
  computed: {
    ...mapGetters(["getMethod", "getUserId", "getUrl", "getTime"]),
    changeData() {
      return this.data;
    },
    currentUser() {
      return this.$store.state.auth.user;
    }
  },
  watch: {
    $route(to, from) {
      if (to !== from) {
        location.reload();
      }
    }
  },
  methods: {
    async getData() {
      let response = "";
      this.page = parseInt(this.$route.query.page) || 1;
      if (this.$route.query.method) {
        let query = `?method=${this.$route.query.method}&page=${this.page}`;
        if (this.$route.query.user_id) {
          this.$store.commit("setUserId", this.$route.query.user_id);
          query += `&user_id=${this.$route.query.user_id}`;
        }
        if (this.$route.query.url) {
          this.$store.commit("setUrl", this.$route.query.url);
          query += `&url=${this.$route.query.url}`;
        }
        if (this.$route.query.time_from) {
          this.$store.commit("setTime", this.$route.query.time_from);
          query += `&time_from=${this.$route.query.time_from}`;
        }
        response = await UserService.getUserBoard(
          `${Api.DASHBOARD_FILTER}` + query
        );
      } else {
        response = await UserService.getUserBoard(
          `${Api.DASHBOARD}?page=${this.page}`
        );
      }
      this.totalpage = Math.ceil(response.data.counts / 10);
      this.data = response.data.results.map((item, id) => {
        if (!item.user_id) {
          item.user_id = "Anonymous";
        }
        return { ...item, id };
      });
    },
    filterFuntion() {
      this.page = 1;
      const query = {};
      query.method = this.getMethod;
      query.page = this.page;
      if (this.getUserId) {
        query.user_id = this.getUserId;
      }
      if (this.getUrl) {
        query.url = this.getUrl;
      }
      if (this.getTime) {
        query.time_from = this.getTime;
      }
      this.$router.push({
        name: "Dashboard",
        query: query
      });
    },
    getBadge(request_method) {
      switch (request_method) {
        case "GET":
          return "success";
        case "OPTIONS":
          return "secondary";
        case "POST":
          return "warning";
        case "DELETE":
          return "danger";
        default:
          "primary";
      }
    },
    toggleDetails(item) {
      this.$set(this.data[item.id], "_toggled", !item._toggled);
      this.collapseDuration = 300;
      this.$nextTick(() => {
        this.collapseDuration = 0;
      });
    },
    getResultPage(page) {
      this.page = page;
      this.$router.push({
        path: this.$route.fullPath,
        query: { page: this.page }
      });
    }
  }
};
</script>

<style lang="css">
.button-table {
  font-size: 25px;
  text-align: right;
}
</style>
