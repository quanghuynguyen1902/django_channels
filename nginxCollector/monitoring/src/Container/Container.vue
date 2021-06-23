<template>
  <div class="c-app">
    <Sidebar />
    <CWrapper>
      <Navbar />
      <div class="c-body">
        <main class="c-main">
          <CContainer fluid>
            <transition name="fade" mode="out-in">
              <router-view :key="$route.path" />
              <Intruction></Intruction>
            </transition>
          </CContainer>
        </main>
      </div>
      <Footer />
    </CWrapper>
  </div>
</template>

<script>
import Sidebar from "@/components/Sidebar";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import Intruction from "@/components/Instruction";
export default {
  name: "Container",
  components: {
    Sidebar,
    Navbar,
    Footer,
    Intruction
  }
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
