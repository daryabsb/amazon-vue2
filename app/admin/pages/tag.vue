<template>
  <main>
    <div class="container-fluid c-section">
      <div class="row">
        <div class="col-sm-3"></div>
        <div class="col-sm-6">
          <div class="a-spacing-top-medium" style="text-align: center"></div>
          <h2>Add a new Tag</h2>
          <form>
            <div class="a-spacing-top-medium">
              <label>Tag</label>
              <input type="text" class="a-input-text" 
              style="width: 100%;" v-model="tag" />
            </div>
            <hr />
            <!-- Button -->
            <div class="a-spacing-top-large">
              <span class="a-button-register">
                <span class="a-button-inner">
                  <span class="a-button-text" 
                  @click="onAddTag"
                  >Add Tag</span>
                </span>
              </span>
            </div>
          </form>
          <div class="a-spacing-top-medium" style="text-align: center"></div>
          <ul class="list-group-item">
            <li v-for="tag in tags" 
            :key="tag.id"
            >{{tag.name}}</li>
          </ul>
        </div>
        <div class="col-sm-3"></div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  async asyncData({ $axios }) {
    try {
      let response = await $axios.$get('/product/tags/');
    //   console.log(response);
      return {
        tags: response
      };
    } catch (err) {
      console.log(err);
    }
  },
  data() {
      return {
           tag: ""
      };
   
  },
  methods: {
    async onAddTag() {
      try {
        let data = { name: this.tag };
        let response = await this.$axios.$post(
            "/product/tags/", data);
            this.tags.push(data);
      } catch (err) {
        console.log(err);
      }
    //   
    }
  }
}
</script>