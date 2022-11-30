<template>
  <v-container fill-height fluid>
    <v-row>
      <v-col align="center" justify="center">
        <div class="ma-10" style="width: 50em">
          <div class="lab-name-chinese">塵間感知與雲端計算實驗室</div>
          <div class="lab-name-english mb-10">
            Ubiquitous Sensing and Cloud Computing Lab
          </div>
          <v-btn
            class="mr-10 secondary--text"
            href="https://plato.csie.ncku.edu.tw/"
            target="_blank"
            outlined
          >
            實驗室網站
          </v-btn>
          <v-btn
            class="secondary--text"
            outlined
            @click="$router.push({ path: '/chatbot' })"
          >
            問答機器人
          </v-btn>
        </div>
        <div class="mt-10">
          <iframe
            width="600em"
            height="350em"
            :src="introduce_youtube_link"
            frameborder="0"
            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
          >
          </iframe>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HomeView",
  data() {
    return {
      introduce_youtube_link: "",
      youtubeURL:
        "https://www.youtube.com/watch?v=paM9JV-NJg8&ab_channel=MikeChou",
    };
  },
  mounted() {
    const youtubeEmbedTemplate = "https://www.youtube.com/embed/";
    const url = this.youtubeURL.split(
      /(vi\/|v%3D|v=|\/v\/|youtu\.be\/|\/embed\/)/
    );
    const YId =
      undefined !== url[2] ? url[2].split(/[^0-9a-z_/\\-]/i)[0] : url[0];
    const topOfQueue = youtubeEmbedTemplate.concat(YId);
    this.introduce_youtube_link = topOfQueue;
  },
  components: {},
};
</script>

<style scoped>
.lab-name-chinese {
  font-size: 4em;
  font-weight: 100;
}
.lab-name-english {
  font-size: 2em;
  font-weight: 10;
}
</style>
