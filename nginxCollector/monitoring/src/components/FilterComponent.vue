<template>
  <div>
    <CRow>
      <CCol sm="6">
        <CInput
          v-model="user_id"
          label="User Id"
          placeholder="Enter user id"
          @input="$store.commit('setUserId', user_id)"
        />
      </CCol>
      <CCol sm="6">
        <CSelect
          label="Method"
          :options="['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']"
          :value.sync="method"
          @update:value="$store.commit('setMethod', method)"
        />
      </CCol>
    </CRow>
    <CRow>
      <CCol sm="6">
        <CInput
          v-model="url"
          label="Url"
          placeholder="Enter url"
          @input="$store.commit('setUrl', url)"
        />
      </CCol>
      <CCol sm="6">
        <CInput
          v-model="time_from"
          label="Time from"
          type="date"
          @input="$store.commit('setTime', time_from)"
        />
      </CCol>
    </CRow>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "FilterComponent",
  data() {
    return {
      item: 1,
      method: "",
      user_id: "",
      url: "",
      time_from: ""
    };
  },
  mounted() {
    if (this.$route.query.method) {
      this.method = this.$route.query.method;
    } else {
      this.method = this.getMethod;
    }
    if (this.$route.query.user_id) {
      this.user_id = this.$route.query.user_id;
    }
    if (this.$route.query.url) {
      this.url = this.$route.query.url;
    }
    if (this.$route.query.time_from) {
      this.time_from = this.$route.query.time_from;
    }
  },
  computed: {
    ...mapGetters(["getMethod", "getUserId", "getUrl", "getTime"])
  }
};
</script>
