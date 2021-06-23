<template>
  <CRow>
    <CCol sm="12">
      <CRow>
        <CCol sm="12">
          <CCallout color="success">
            <small class="text-muted">Total request</small><br />
            <strong class="h4">{{ total }}</strong>
          </CCallout>
        </CCol>
      </CRow>
      <hr class="mt-0" />
      <ul class="horizontal-bars type-2">
        <div
          v-for="(method, index) in methods"
          :key="index"
          class="progress-group"
        >
          <div class="progress-group-header">
            <span class="title">{{ method.name }}</span>
            <span class="ml-auto font-weight-bold">
              {{ method.count }}
              <span class="text-muted small"
                >{{ (method.count / total).toFixed(2) * 100 }} %
              </span>
            </span>
          </div>
          <div class="progress-group-bars">
            <CProgress
              class="progress-xs"
              :value="(method.count / total).toFixed(2) * 100"
              color="success"
            />
          </div>
        </div>
      </ul>
    </CCol>
  </CRow>
</template>
<script>
import UserService from "../../api/userService";
import Api from "@/constants/backendApi";
export default {
  name: "MethodChart",
  data() {
    return {
      total: 0,
      methods: {}
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    async getData() {
      const response = await UserService.getUserBoard(
        `${Api.REQUESTS_ANALYTIC}?user_id=${this.$route.params.user_id}`
      );
      this.total = response.data.total;
      console.log(this.total);
      this.methods = response.data.methods;
    }
  }
};
</script>
