<template>
  <div class="c-app flex-row align-items-center">
    <CContainer>
      <CRow class="justify-content-center">
        <CCol md="8">
          <CCardGroup>
            <CCard class="p-4">
              <CCardBody>
                <CForm>
                  <h1>Login</h1>
                  <p class="text-muted">Sign In to your account</p>
                  <CInput
                    v-model="user.email"
                    placeholder="Email"
                    autocomplete="email"
                  >
                    <template #prepend-content
                      ><CIcon name="cil-user"
                    /></template>
                  </CInput>
                  <CInput
                    v-model="user.password"
                    placeholder="Password"
                    type="password"
                    autocomplete="curent-password"
                  >
                    <template #prepend-content
                      ><CIcon name="cil-lock-locked"
                    /></template>
                  </CInput>
                  <div class="message-error">{{ message }}</div>
                  <CRow>
                    <CCol col="6" class="text-left">
                      <CButton color="primary" class="px-4" @click="handleLogin"
                        >Login</CButton
                      >
                    </CCol>
                    <CCol col="6" class="text-right">
                      <!--                      <CButton color="link" class="px-0"-->
                      <!--                        >Forgot password?</CButton-->
                      <!--                      >-->
                      <CButton color="link" class="d-lg-none"
                        >Register now!</CButton
                      >
                    </CCol>
                  </CRow>
                </CForm>
              </CCardBody>
            </CCard>
            <CCard
              color="primary"
              text-color="white"
              class="text-center py-5 d-md-down-none"
              body-wrapper
            >
              <CCardBody>
                <h2>Sign up</h2>
                <CButton
                  color="light"
                  variant="outline"
                  size="lg"
                  @click="register"
                >
                  Register Now!
                </CButton>
              </CCardBody>
            </CCard>
          </CCardGroup>
        </CCol>
      </CRow>
    </CContainer>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      user: {
        email: "",
        password: ""
      },
      message: ""
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    }
  },
  created() {
    if (this.loggedIn) {
      this.$router.push("/");
    }
  },
  methods: {
    handleLogin() {
      if (!this.user.email || !this.user.password) {
        this.message = "Please, enter correct email and correct password";
      } else {
        this.$store.dispatch("auth/login", this.user).then(
          () => {
            this.$router.push("/");
          },
          error => {
            console.log(error);
            this.message = "Authenticaton failed";
          }
        );
      }
    },
    register() {
      this.$router.push("/register");
    }
  }
};
</script>

<style>
.message-error {
  margin-bottom: 25px;
  color: #ff5559;
}
</style>
