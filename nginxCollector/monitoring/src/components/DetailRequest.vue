<template>
  <CCardBody style="background-color: #fffaf1">
    <CRow>
      <CCol sm="3">
        <span class="d-block font-weight-bold">Created at</span>
        <span class="d-block">{{ convertTime }}</span>
      </CCol>
      <CCol sm="3">
        <span class="d-block font-weight-bold">User</span>
        <span class="d-block">
          <ul
            v-for="(value, key, index) in item.user"
            :key="index"
            class="user-detail-show"
          >
            <li>{{ key }}: {{ value }}</li>
          </ul>
        </span>
      </CCol>
      <CCol sm="3">
        <span class="d-block font-weight-bold">Request time</span>
        <span class="d-block">{{ item.request_time }}</span>
      </CCol>
      <CCol sm="3">
        <span class="d-block font-weight-bold">Size</span>
        <span class="d-block">{{ item.size }}</span>
      </CCol>
    </CRow>
  </CCardBody>
</template>

<script>
export default {
  name: "DetailRequest",
  props: {
    item: {
      type: Object
    }
  },
  computed: {
    convertTime() {
      return new Date(parseFloat(this.item.created_at) * 1000).toGMTString();
    }
  }
};
</script>

<style lang="scss">
.user-detail-show {
  padding: 0;
  li {
    display: block;
  }
}
</style>
