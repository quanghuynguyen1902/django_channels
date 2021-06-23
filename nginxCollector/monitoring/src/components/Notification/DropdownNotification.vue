<template>
  <CDropdown in-nav class="c-header-nav-items" add-menu-classes="pt-0">
    <template #toggler>
      <CHeaderNavLink>
        <div class="notification" @click="getNotification">
          <CIcon size="lg" name="cil-bell" />
          <span v-if="notification_count > 0" class="badge">{{
            notification_count
          }}</span>
        </div>
      </CHeaderNavLink>
    </template>
    <CDropdownHeader
      tag="div"
      class="text-center h6 d-flex justify-content-between border-bottom m-0"
    >
      <strong>Notification</strong>
      <div class="mark-notification" @click="markAllReaded">
        Mark all as read
      </div>
    </CDropdownHeader>
    <div v-for="(notify, index) in notifications" :key="index">
      <NotificationItem
        :notify="notify"
        :allReaded="allReaded"
      ></NotificationItem>
    </div>
  </CDropdown>
</template>

<script>
import Api from "@/constants/backendApi";
import UserService from "../../api/userService";
import NotificationItem from "@/components/Notification/NotificationItem";
export default {
  name: "DropdownNotification",
  components: {
    NotificationItem
  },
  data() {
    return {
      notification_count: 0,
      notifications: [],
      allReaded: false,
      interval: null
    };
  },
  // mounted() {
  //   this.getNotificationCount();
  //   if (!this.interval) {
  //     this.interval = setInterval(this.updateNotification, 10000);
  //   }
  // },
  beforeDestroy() {
    if (this.interval) {
      clearInterval(this.interval);
    }
  },
  methods: {
    async getNotificationCount() {
      const response = await UserService.getUserBoard(Api.NOTIFICATION_COUNT);
      this.notification_count = response.data[0].quantity;
    },
    async getNotification() {
      this.notification_count = 0;
      const response = await UserService.getUserBoard(Api.NOTIFICATION);
      this.notifications = response.data;
    },
    async updateNotification() {
      if (this.$store.state.auth.status.loggedIn) {
        const count = await UserService.getUserBoard(Api.NOTIFICATION_COUNT);
        this.notification_count = count.data[0].quantity;
        if (this.countNotify > 9) {
          this.notification_count = "9+";
        }
      }
    },
    markAllReaded() {
      this.allReaded = true;
      this.notification_count = 0;
      for (const notify of this.notifications) {
        UserService.getUserBoard(`${Api.NOTIFICATION}` + `${notify.slug}/`);
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.c-icon {
  margin-right: 0.3rem;
}

.mark-notification {
  color: #2faff7;
  &:hover {
    color: #077cdd;
  }
  cursor: pointer;
}
.dropdown-menu.show {
  height: 800px;
}
.notification {
  position: relative;
  .badge {
    position: absolute;
    top: -5px;
    right: -5px;
    padding: 2px 2px;
    border-radius: 50%;
    background-color: red;
    color: white;
  }
}
</style>
