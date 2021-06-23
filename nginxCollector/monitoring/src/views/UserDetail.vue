<template>
  <div>
    <CRow>
      <CCol md="12">
        <CCard>
          <CCardHeader>
            Requests
          </CCardHeader>
          <CCardBody>
            <method-chart></method-chart>
            <br />
          </CCardBody>
        </CCard>
      </CCol>
      <CCol md="12">
        <CCard>
          <UserListTable></UserListTable>
        </CCard>
      </CCol>
    </CRow>
  </div>
</template>
<script>
import MethodChart from "@/components/charts/MethodChart";
import UserListTable from "@/components/user-detail/UserListTable";
export default {
  name: "UserDetail",
  components: {
    UserListTable,
    MethodChart
  }
};
</script>
