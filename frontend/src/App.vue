<template>
  <v-app>
    <v-app-bar app class="light-bar" color="primary" dark>
      <div class="d-flex align-center">
        <span
          class="font-weight-thin text-h5 white--text"
          style="cursor: pointer"
          @click="$router.push({ path: '/' })"
        >
          塵間感知與雲端計算實驗室 USCC
        </span>
      </div>

      <v-spacer></v-spacer>
      <v-btn
        v-if="!isLogin"
        text
        class="mx-1"
        @click="$router.push({ path: '/login' })"
      >
        <v-icon>mdi-account</v-icon>
      </v-btn>

      <v-btn v-if="isLogin" text class="mx-1" @click="signOut">
        <v-icon>mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
  computed: {
    isLogin: {
      get() {
        if (this.$cookies.isKey("user_id") == false) return false;
        else return true;
      },
    },
  },
  methods: {
    signOut: function () {
      this.$cookies.remove("user_id");
      this.$toast.info("Successfully logged out", {
        position: "top-center",
        timeout: 2000,
      });
      this.$router.push({ path: "/" });
    },
  },
};
</script>

<style scoped>
@import "@/assets/styles/app-bar/light-bar.css";
</style>
