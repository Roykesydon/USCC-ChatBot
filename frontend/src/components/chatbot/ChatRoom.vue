<template>
  <v-card class="pa-0" fill-height elevation="20">
    <v-card-title
      class="primary_dark primary--text text-h4 pa-7 font-weight-bold d-flex align-center"
      style="background-color: #303030"
    >
      <v-icon color="primary" size="30" class="mr-5">mdi-robot</v-icon>
      <div>USCC 問答機器人</div>
    </v-card-title>
    <!-- <v-divider></v-divider> -->
    <v-card-text
      class="text-h5 font-weight-thin pa-7"
      style="height: 60vh; overflow-y: scroll; background-color: #060606"
    >
      <v-row
        class="flex-column mx-5"
        v-for="(message, index) in messages"
        :align="messageAlign(message)"
        :key="index"
      >
        <div class="mb-10">
          <v-row :class="idJustify(message.self)">
            <span class="text-h6 font-weight-thin secondary--text">{{
              message.nickname
            }}</span>
            <span class="text-h6 font-weight-thin grey--text"
              >@{{ message.username }}</span
            >
          </v-row>
          <v-row :class="idJustify(message.self)">
            <v-card
              class="grey darken-4 py-1 px-3 white--text text-wrap"
              style="
                white-space: pre-wrap;
                word-wrap: break-word;
                font-family: inherit;
              "
              max-width="20vw"
            >
              <div
                v-for="(line, lineNumber) of message.msg.split('\n')"
                v-bind:key="lineNumber"
              >
                {{ line }}
              </div>
            </v-card>
          </v-row>
        </div>
      </v-row>
    </v-card-text>
    <v-form ref="queryForm" v-model="queryFormValid" lazy-validation>
      <v-card-actions style="background-color: #303030">
        <v-text-field
          v-model="message"
          label="輸入問題，勿超過 50 字"
          class="ml-2"
          color="primary"
          :rules="[rules.chatbotQuery]"
          outlined
          dense
          hide-details
        ></v-text-field>
        <v-btn color="primary" outlined class="mx-3" @click="sendQuestion">
          send
        </v-btn>
      </v-card-actions>
    </v-form>
  </v-card>
</template>
<script>
import { rules } from "@/jsLibrary/rules.js";
import { apiAddress } from "@/config.js";

export default {
  name: "ChatRoom",
  components: {},
  async mounted() {
    this.messages.push({
      username: "uscc_chatbot",
      nickname: "問答機器人",
      msg: "哈囉！有什麼有關實驗室的問題要問的嗎？",
      self: false,
    });
  },
  data() {
    return { messages: [], message: "", rules: rules, queryFormValid: true };
  },
  methods: {
    idJustify: function (self) {
      if (self) return "d-flex justify-end";
      return "";
    },
    messageAlign: function (message) {
      if (message.self) return "end";

      return "start";
    },
    sendQuestion: async function () {
      if (this.message == "") return;

      if (this.$refs.queryForm.validate() == false) {
        return;
      }

      let _this = this;
      this.messages.push({
        username: this.$cookies.get("user_id"),
        nickname: "使用者",
        msg: this.message,
        self: true,
      });

      let message = this.message;
      this.message = "";

      await this.$axios
        .get(apiAddress + "/chatbot/query", {
          params: {
            text: message,
          },
        })
        .then((response) => {
          if (response.data.success == 1) {
            console.log(response.data.text);
            _this.messages.push({
              username: "uscc_chatbot",
              nickname: "問答機器人",
              msg: response.data.text,
              self: false,
            });
          } else {
            _this.$toast.error(response.data.msg, {
              position: "top-center",
              timeout: 2000,
            });
          }
        })
        .catch((error) => {
          console.log(error);
          _this.$toast.error("發生錯誤", {
            position: "top-center",
            timeout: 2000,
          });
        });
    },
  },
};
</script>

<style scope>
/* custom scrollbar */
::-webkit-scrollbar {
  width: 20px;
}

::-webkit-scrollbar-track {
  background-color: transparent;
}

::-webkit-scrollbar-thumb {
  background-color: #d6dee1;
  border-radius: 20px;
  border: 6px solid transparent;
  background-clip: content-box;
}

::-webkit-scrollbar-thumb:hover {
  background-color: #a8bbbf;
}
</style>
