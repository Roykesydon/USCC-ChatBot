<template>
  <v-card class="pa-10">
    <div class="ma-5">
      <loading
        :active.sync="isLoading"
        :can-cancel="false"
        :is-full-page="false"
        :color="$vuetify.theme.currentTheme.primary"
        :background-color="$vuetify.theme.currentTheme.customBackground"
      ></loading>
      <div class="text-h2 font-weight-thin text-center primary--text dark">
        Login
      </div>
      <div class="my-auto pa-10">
        <v-form ref="signInForm" v-model="signInValid" lazy-validation>
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="inputUserID"
                label="User ID"
                :rules="[rules.required, rules.englishAndNumberOnly, rules.id]"
              ></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field
                v-model="inputPassword"
                label="Password"
                :type="showPassword ? 'text' : 'password'"
                :rules="[
                  rules.required,
                  rules.englishAndNumberOnly,
                  rules.password,
                ]"
                :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                @click:append="showPassword = !showPassword"
              ></v-text-field>
            </v-col>
          </v-row>
          <div class="d-flex justify-end">
            <v-spacer></v-spacer>
            <!-- <v-btn
              color="primary"
              text
              @click="$emit('closeSignInUpInterface')"
            >
              Close
            </v-btn> -->
            <v-btn color="primary" text @click="login()"> Login </v-btn>
          </div>
          <!-- <div class="d-flex justify-end my-5">
            <v-btn color="secondary" text @click="$emit('wantToSignUp')">
              don't have acoount?
            </v-btn>
          </div> -->
        </v-form>
      </div>
    </div>
  </v-card>
</template>

<script>
import { rules } from "@/jsLibrary/rules.js";
import { apiAddress } from "@/config.js";

import Loading from "vue-loading-overlay";
import "vue-loading-overlay/dist/vue-loading.css";

export default {
  name: "LoginForm",
  components: {
    Loading,
  },
  data: () => ({
    inputUserID: "",

    inputPassword: "",
    showPassword: false,

    signInValid: true,

    isLoading: false,

    rules: rules,
  }),
  methods: {
    requestLogin: async function () {
      let user_id = this.inputUserID;
      await this.$axios
        .post(apiAddress + "/user/login", {
          userID: user_id,
          password: this.inputPassword,
        })
        .then((response) => {
          if (response.data.success == 1) {
            this.$cookies.set("user_id", user_id);
            this.$toast.success("Login Success!", {
              position: "top-center",
              timeout: 2000,
            });
            this.$router.push({ path: "/" });
          } else {
            this.$toast.error(response.data.msg, {
              position: "top-center",
              timeout: 2000,
            });
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    login: async function () {
      if (this.$refs.signInForm.validate() == false) {
        return;
      }

      this.isLoading = true;
      await this.requestLogin();
      this.isLoading = false;
    },
  },
};
</script>
