<template>
  <v-container fill-height fluid>
    <v-row align="center" justify="center">
      <v-col
        ><login-form class="login-form ma-auto my-auto"></login-form
      ></v-col>
    </v-row>
  </v-container>
</template>

<script>
import LoginForm from "@/components/user/LoginForm.vue";

export default {
  name: "LoginView",

  components: {
    LoginForm,
  },
};
</script>

<style scoped>
.login-form {
  height: 50vh;
  width: 35vw;
}
</style>
