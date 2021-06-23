<template>
  <div class="mx-auto mt-lg-5" style="width: 60%;">
    <CRow>
      <CCol sm="12">
        <CCard>
          <CCardHeader
            class="p-4"
            color="info"
            style="font-size: 1.2rem; color: white"
          >
            Set up your app information
          </CCardHeader>
          <CCardBody>
            <div class="set-up">
              <h6>
                1. Please enter field in header which has token authentication
              </h6>
              <CInput v-model="auth_field" placeholder="Enter your field" />
              <h6>
                2. Please enter your api to identify user from your app
              </h6>
              <CInput v-model="auth_api" placeholder="Enter your api" />
            </div>
            <div class=""></div>
          </CCardBody>
          <CCardFooter>
            <div class="text-end">
              <c-button color="info" @click="Update">Done</c-button>
            </div>
          </CCardFooter>
        </CCard>
      </CCol>
    </CRow>
  </div>
</template>

<script>
import UserService from "../api/userService";
import Api from "@/constants/backendApi";
import authHeader from "../api/authHeader";
import axios from "axios";
export default {
  name: "Information",
  data() {
    return {
      auth_field: "",
      auth_api: ""
    };
  },
  mounted() {
    this.getInformation();
  },
  methods: {
    async getInformation() {
      const response = await UserService.getUserBoard(Api.INFORMATION);
      this.auth_api = response.data.api_identify;
      this.auth_field = response.data.authorization_field;
    },
    async Update() {
      const response = await axios.put(
        `http://127.0.0.1:8001/api/users/${this.$store.state.auth.user.slug}/update-user/`,
        { api_identify: this.auth_api, authorization_field: this.auth_field },
        { headers: authHeader() }
      );
      console.log(response);
    }
  }
};
</script>

<style lang="scss">
.set-up {
  font-family: "Courier";
  margin-bottom: 10px;
  white-space: pre;
  border-radius: 3px;
  overflow: auto;
  line-height: 1.4;
  padding: 7px;
  cursor: pointer;
}
h6 {
  font-weight: bold !important;
}
</style>
