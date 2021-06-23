<template>
  <div
    @click="checkReadNotify"
    :class="['notification-item', isReaded || allReaded ? 'read' : 'unread']"
  >
    <div class="py-2">
      <CIcon style="color: #e2a209" name="cil-warning" />
    </div>
    <div class="mx-3">
      <div class="notify-content">{{ notify.content }}</div>
      <div class="notify-create">
        <CIcon style="width: 0.7rem; height: 0.7rem" name="cil-clock" />
        {{ timeWithAgoFormat }}
      </div>
    </div>
  </div>
</template>

<script>
import { TimeUtil } from "@/util/timeUtils";
import Api from "@/constants/backendApi";
import UserService from "../../api/userService";
export default {
  props: {
    notify: {
      type: Object
    },
    allReaded: {
      type: Boolean,
      default: false
    }
  },
  mounted() {
    if (this.notify.status === "U") {
      this.isReaded = false;
    } else {
      this.isReaded = true;
    }
  },
  data() {
    return {
      isReaded: false
    };
  },
  computed: {
    timeWithAgoFormat() {
      return TimeUtil.formatTimeAgo(this.notify.created_at);
    }
  },
  methods: {
    async checkReadNotify() {
      this.isReaded = true;
      await UserService.getUserBoard(
        `${Api.NOTIFICATION}` + `${this.notify.slug}` + "/"
      );
    }
  }
};
</script>

<style lang="scss">
.notification-item {
  min-width: 500px;
  max-width: 800px;
  padding: 10px;
  border-bottom: 1px dashed #c0c0c0;
  color: #000;
  display: flex;
  background-color: #fff;
  &:hover {
    background-color: #f6f6f6;
  }
  cursor: pointer;
}

.notification-item.unread {
  background-color: #f0f0f0;
}

.notify-content {
  font-size: 1.2em;
}
.notify-create {
  font-size: 12px;
  font-weight: 100;
}
</style>
