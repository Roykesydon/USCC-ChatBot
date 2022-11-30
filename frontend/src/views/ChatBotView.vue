<template>
  <v-container fill-height fluid>
    <v-row align="center" justify="center">
      <v-col><chat-room class="chat-room ma-auto my-auto"></chat-room></v-col>
    </v-row>
  </v-container>
</template>

<script>
import ChatRoom from "@/components/chatbot/ChatRoom.vue";

export default {
  name: "ChatBotView",
  components: {
    ChatRoom,
  },
  mounted() {
    if (this.$cookies.isKey("user_id") == false) {
      this.$toast.info("請先登入", {
        position: "top-center",
        timeout: 2000,
      });
      this.$router.push({ path: "/login" });
    }
  },
};
</script>

<style scoped>
.chat-room {
  height: 70vh;
  width: 35vw;
}
</style>
