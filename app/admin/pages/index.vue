<template>
  <main>
    <div class="a-spacing-large"></div>
    <!-- <h3 v-for="(product, index) in products" :key="index">
      {{ product.title }} <br/>
    </h3> -->
    <div class="containerfluid browsing-history">
      <div class="row">
        <div class="col-sm-8 col-8">
          <h1 class="a-size-large a-spacing-none a-text-normal">All Products</h1>
          <div class="a-spacing-large"></div>
          <!-- Button -->
          <a href="#" class="a-button-buy-again">Add a new product</a>
          <a href="#" class="a-button-history margin-right-10">Add a new category</a>
          <a href="#" class="a-button-history margin-right-10">Add a new owner</a>
          <!-- Listing Page -->
        </div>
      </div>
    </div>

    <div class="a-spacing-large"></div>

    <div class="containerfluid browsing-history">
      <div class="row">
        <div 
        v-for="product in products" :key="product.id"
        class="col-xl-2 col-lg-2 col-md-3 col-sm-6 col-6 br bb">
          <div class="history-box">
            <div class="text-center">
              <!-- Product Image -->
              <a href="#" class="a-link-normal">
                <img :src="product.image" class="img-fluid" />
              </a>
              <!-- Product Title -->
              <div class="a-spacing-top-base asin-title">
                <span class="a-text-normal">
                  <div class="p13n-sc-truncated">{{product.title}}</div>
                </span>
              </div>
              <!-- Product Rating -->
              <div class="a-row">
                <a href="#">
                  <i class="fas fa-star"></i>
                  <i class="fas fa-star"></i>
                  <i class="fas fa-star"></i>
                  <i class="fas fa-star"></i>
                  <i class="fas fa-star"></i>
                </a>
                <span class="a-letter-space"></span>
                <span class="a-color-tertiary a-size-small asin-reviews">(1732)</span>
              </div>

              <!-- Product Price -->
              <div class="a-row">
                <span class="a-size-base a-color-price">
                  <span class="p13n-sc-price">{{product.price}}</span>
                </span>
              </div>
              <!-- Product Buttons -->
              <div class="a-row">
                <a href="" class="a-button-history margin-right-10">Update</a>
                <a href="" class="a-button-history margin-right-10">Delete</a>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  </main>
</template>

<script>
export default {
  // asyncData is fetching data before nuxt page finished loading on the browser
  // It is good for SEO because the data will be loaded first
  async asyncData({ $axios }) {
    try {
      // let response = await this.$axios.$get(`${baseURL}/product/myproducts`);
      let response = await $axios.$get('/product/myproducts/');

     // console.log(response);

      return {
        products: response
      }

    } catch (err) {
      console.log("Your api is not working")
    }
    
    
  }
}
</script>

<style>
</style>



// .container {
//   margin: 0 auto;
//   min-height: 100vh;
//   display: flex;
//   justify-content: center;
//   align-items: center;
//   text-align: center;
// }

// .title {
//   font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
//     'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
//   display: block;
//   font-weight: 300;
//   font-size: 100px;
//   color: #35495e;
//   letter-spacing: 1px;
// }

// .subtitle {
//   font-weight: 300;
//   font-size: 42px;
//   color: #526488;
//   word-spacing: 5px;
//   padding-bottom: 15px;
// }

// .links {
//   padding-top: 15px;
// }
