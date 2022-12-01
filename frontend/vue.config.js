const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  transpileDependencies: ["vuetify"],
});

module.exports = {
  devServer: {
    allowedHosts: "all",
    port: 80,
  },
};
