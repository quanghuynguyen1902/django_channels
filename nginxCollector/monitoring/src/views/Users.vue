<template>
  <CRow>
    <CCol col="12" xl="8">
      <CCard>
        <CCardHeader>
          Users
        </CCardHeader>
        <CCardBody>
          <CDataTable
            hover
            striped
            :items="items"
            :fields="fields"
            :items-per-page="5"
            clickable-rows
            :active-page="activePage"
            @row-clicked="rowClicked"
            :pagination="{ doubleArrows: false, align: 'center' }"
            @page-change="pageChange"
          >
          </CDataTable>
        </CCardBody>
      </CCard>
    </CCol>
  </CRow>
</template>

<script>
import Api from "@/constants/backendApi";
import UserService from "../api/userService";
export default {
  name: "Users",
  data() {
    return {
      items: [],
      fields: [{ key: "user_id" }],
      activePage: 1
    };
  },
  mounted() {
    this.get_users();
  },
  methods: {
    async get_users() {
      const response = await UserService.getUserBoard(Api.USERS);
      for (let key of response.data.keys) {
        this.fields.push({ key: key });
      }
      this.items = response.data.results;
    },
    rowClicked(item) {
      this.$router.push({ path: `/users/${item.user_id}` });
    },
    pageChange(val) {
      this.$router.push({ query: { page: val } });
    }
  }
};
</script>
