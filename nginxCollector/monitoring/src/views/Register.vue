<template>
  <div class="d-flex align-items-center min-vh-100">
    <CContainer fluid>
      <CRow class="justify-content-center">
        <CCol md="6">
          <CCard class="mx-4 mb-0">
            <CCardBody class="p-4">
              <CForm>
                <h1>Register</h1>
                <p class="text-muted">Create your account</p>
                <CInput
                  v-model="user.username"
                  placeholder="Username"
                  autocomplete="username"
                >
                  <template #prepend-content><CIcon name="cil-user"/></template>
                </CInput>
                <CInput
                  v-model="user.email"
                  placeholder="Email"
                  autocomplete="email"
                  prepend="@"
                />
                <CInput
                  v-model="user.password"
                  placeholder="Password"
                  type="password"
                  autocomplete="new-password"
                >
                  <template #prepend-content
                    ><CIcon name="cil-lock-locked"
                  /></template>
                </CInput>
                <CInput
                  v-model="user.password2"
                  placeholder="Repeat password"
                  type="password"
                  autocomplete="new-password"
                  class="mb-4"
                >
                  <template #prepend-content
                    ><CIcon name="cil-lock-locked"
                  /></template>
                </CInput>
                <div v-if="successful && message" class="message-successful">
                  {{ message }}
                </div>
                <div v-else class="message-error">{{ message }}</div>
                <CButton color="info" block @click="handleRegister"
                  >Create Account</CButton
                >
              </CForm>
            </CCardBody>
            <CCardFooter class="p-4"> </CCardFooter>
          </CCard>
        </CCol>
      </CRow>
    </CContainer>
  </div>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      user: {
        username: "",
        password: "",
        email: "",
        password2: ""
      },
      submitted: false,
      successful: false,
      message: ""
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    }
  },
  mounted() {
    if (this.loggedIn) {
      this.$router.push("/");
    }
  },
  methods: {
    handleRegister() {
      this.message = "";
      if (
        !this.user.email ||
        !this.user.username ||
        !this.user.password ||
        !this.user.password2
      ) {
        this.message =
          "Please, enter correct email, correct username and correct password";
        return;
      }
      if (this.user.password != this.user.password2) {
        this.message = "Passwords do not match";
        return;
      } else if (!this.validEmail(this.user.email)) {
        this.message = "Valid email required";
        return;
      }
      this.$store.dispatch("auth/register", this.user).then(
        () => {
          this.message = "Register successful";
        },
        error => {
          this.message = error.response.data.email[0];
          this.successful = false;
        }
      );
    },
    validEmail(email) {
      var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(email);
    }
  }
};
</script>
<style lang="scss">
.message-successful {
  margin-bottom: 25px;
  color: #42ff42;
}
.message-error {
  margin-bottom: 25px;
  color: #ff5559;
}
</style>
