<template>
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
        <CCollapse :show="Boolean(item._toggled)" :duration="collapseDuration">
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
</template>
<script>
import UserService from "../../api/userService";
import Api from "@/constants/backendApi";
import DetailRequest from "@/components/DetailRequest";
export default {
  name: "UserListTable",
  components: {
    DetailRequest
  },
  data() {
    return {
      data: [],
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
      page: 1,
      totalpage: 1
    };
  },
  mounted() {
    this.getData();
  },
  watch: {
    $route(to, from) {
      if (to !== from) {
        location.reload();
      }
    }
  },
  computed: {
    changeData() {
      return this.data;
    }
  },
  methods: {
    async getData() {
      let response = "";
      this.page = parseInt(this.$route.query.page) || 1;

      response = await UserService.getUserBoard(
        `${Api.USER_DETAILS}?page=${this.page}&user_id=${this.$route.params.user_id}`
      );

      this.totalpage = Math.ceil(response.data.counts / 10);
      this.data = response.data.results.map((item, id) => {
        return { ...item, id };
      });
    },
    getResultPage(page) {
      this.page = page;
      this.$router.push({
        path: this.$route.fullPath,
        query: { page: this.page }
      });
    },
    toggleDetails(item) {
      this.$set(this.data[item.id], "_toggled", !item._toggled);
      this.collapseDuration = 300;
      this.$nextTick(() => {
        this.collapseDuration = 0;
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
    }
  }
};
</script>
