<template>
  <main>
    <div class="cointainer-fluid">
      <div class="row">
        <div class="col-sm-3"></div>
        <div class="col-sm-6">
          <div class="a-section">
            <div class="a-spacing-top-medium"></div>
            <h2 style="text-align: center">Add a new product</h2>
            <form>
              <!-- Category Dropdown -->
              <div class="a-spacing-top-medium">
                <label for>Category</label>
                <select class="a-select-option" v-model="categoryID">
                  <option
                    v-for="category in categories"
                    :key="category.id"
                    :value="category.id"
                    
                  >{{category.name}}</option>
                </select>
              </div>
              <!-- Category Tags -->
              <div class="a-spacing-top-medium">
                <label for>Tags</label>
                <select class="a-select-option">
                  <option 
                  v-for="tag in tags" 
                  :key="tag.id" 
                  :value="tag.id">{{tag.name}}</option>
                </select>
              </div>
              <!-- Titel Text -->
              <div class="a-spacing-top-medium">
                <label style="margin-bottom: 8px;" for="title">Title</label>
                <input type="text" class="a-input-text" style="width: 100%;" v-model="productTitle" />
              </div>
              <!-- Stock Text -->
              <div class="a-spacing-top-medium">
                <label style="margin-bottom: 8px;" for="stock">Stock</label>
                <input
                  type="number"
                  class="a-input-text"
                  style="width: 100%;"
                  v-model="productStock"
                />
              </div>
              <!-- Price Text -->
              <div class="a-spacing-top-medium">
                <label style="margin-bottom: 8px;" for="price">Price</label>
                <input
                  type="number"
                  class="a-input-text"
                  style="width: 100%;"
                  v-model="productPrice"
                />
              </div>
              <!-- Photo file -->
              <div class="a-spacing-top-medium">
                <label style="margin-bottom: 8px;" for="price">Image</label>
                <div class="a-row a-spacing-top-medium">
                  <label class="choosefile-button">
                    <i class="fal fa-plus"></i>
                    <input type="file" @change="onFileSelected" />
                    <p style="margin-top: -70px;">{{ fileName }}</p>
                  </label>
                </div>
                <hr />
                <!-- Button -->
                <div class="a-spacing-top-large">
                  <span class="a-button-register">
                    <span class="a-button-inner">
                      <span class="a-button-text" @click="onAddProduct">Add Product</span>
                    </span>
                  </span>
                </div>
              </div>
            </form>
          </div>
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
      let categories = $axios.$get('/product/categories/')
      let tags = $axios.$get('/product/tags/')

      const [catResponse, tagResponse] = await Promise.all([categories, tags])

      // console.log(catResponse);
      // console.log(tagResponse);

      return {
        categories: catResponse,
        tags: tagResponse
      }
    } catch (err) {
      console.log(err)
      console.log('Please check that your api server is running!')
    }
  },
  data() {
    return {
      categoryID: null,
      tagID: [1],
      productTitle: null,
      productStock: 1,
      productPrice: 0,
      selectedFile: null,
      fileName: ''
    }
  },
  methods: {
    onFileSelected(event) {
      this.selectedFile = event.target.files[0]
      //   console.log(this.selectedFile);
      this.fileName = event.target.files[0].name
      //   console.log(this.fileName);
    },
    async onAddProduct() {
      console.log('tags', this.tagID)
      let formData = new FormData()
      formData.append('category', this.categoryID)
      formData.append('tags', this.tagID[0]),
      formData.append('title', this.productTitle),
      formData.append('stock', this.productStock)
      formData.append('price', this.productPrice)
      formData.append('image', this.selectedFile, this.fileName)

      
      try {
        let result = await this.$axios.$post('/product/myproducts/', formData)
        console.log(formData)
        // console.log("SUCCESS");
        this.$router.push('/')
      } catch (err) {
        console.log('Cannot access the api!')
        console.log(err)
      }
    }
  }
}
</script>