<template>
  <main>
    <div class="container-fluid c-section">
      <div class="row">
        <div class="col-sm-3"></div>
        <div class="col-sm-6">
          <div class="a-spacing-top-medium" style="text-align: center"></div>
          <h2>Add a new category</h2>
          <form>
            <div class="a-spacing-top-medium">
              <label>Category</label>
              <input type="text" class="a-input-text" style="width: 100%;" v-model="cat" />
            </div>
            <hr />
            <!-- Button -->
            <div class="a-spacing-top-large">
              <span class="a-button-register">
                <span class="a-button-inner">
                  <span class="a-button-text" 
                  @click="onAddCategory"
                  >Add Category</span>
                </span>
              </span>
            </div>
          </form>
          <div class="a-spacing-top-medium" style="text-align: center"></div>
          <ul class="list-group-item">
            <li v-for="category in categories" 
            :key="category.id"
            >{{category.name}}</li>
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
      let response = await $axios.$get('/product/categories/');
    //   console.log(response);
      return {
        categories: response
      };
    } catch (err) {
      console.log(err);
    }
  },
  data() {
      return {
           cat: ""
      };
   
  },
  methods: {
    async onAddCategory() {
      try {
        let data = { name: this.cat };
        let response = await this.$axios.$post(
            "/product/categories/", data);
            this.categories.push(data);
      } catch (err) {
        console.log(err);
      }
    //   
    }
  }
}
</script>