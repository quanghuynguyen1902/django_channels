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
            Install nginx collector
          </CCardHeader>
          <CCardBody>
            <div class="install-step">
              <h6>
                1. Install and set up the plugin as follow
                <router-link
                  to="/install-plugin"
                  style="color: #077cdd; text-decoration: underline; cursor: pointer"
                  >link</router-link
                >
              </h6>
            </div>
            <div class="install-step">
              <h6>
                2. Set api_key='key' in file config file in the plugin
              </h6>
              <div class="install-step-1-infor" v-if="isCopied">copied</div>
              <div title="click to copy" class="install-step-1" @click="doCopy">
                {{ api_key }}
              </div>
            </div>
            <div class=""></div>
          </CCardBody>
          <CCardFooter>
            <div class="text-end">
              <c-button color="info" @click="nextFunction">Next</c-button>
            </div>
          </CCardFooter>
        </CCard>
      </CCol>
    </CRow>
  </div>
</template>

<script>
// import UserService from "../api/userService";
// import Api from "@/constants/backendApi";
export default {
  name: "Instruction",
  data() {
    return {
      api_key: "abc",
      isCopied: false
    };
  },
  // mounted() {
  //   this.getApiKey();
  // },
  methods: {
    // async getApiKey() {
    //   const response = await UserService.getUserBoard(Api.API_KEY);
    //   this.api_key = response.data.api_key;
    // },

    doCopy: function() {
      this.isCopied = true;
      var v = this;
      this.$copyText(this.api_key).then(
        function() {},
        function() {
          alert("Can not copy");
        }
      );

      this.$forceUpdate();
      setTimeout(function() {
        v.isCopied = false;
      }, 1000);
    },
    nextFunction() {
      this.$router.push("/information");
    }
  }
};
</script>

<style lang="scss">
.install-step {
  padding: 10px 0;
  border-bottom: 1px solid #dfdfdf;
}
.install-step-1 {
  font-family: "Courier";
  white-space: pre;
  border-radius: 3px;
  background: #eeeeee;
  overflow: auto;
  line-height: 1.4;
  padding: 7px;
  cursor: pointer;
}
.install-step-1-infor {
  font-family: "Courier";
  font-size: 10px;
  white-space: pre;
  border-radius: 3px;
  background: #eeeeee;
  width: max-content;
  margin-bottom: 1px;
}
h6 {
  font-weight: bold !important;
}
</style>
