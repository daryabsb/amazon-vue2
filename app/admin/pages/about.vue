<template>
  <div>
    <h1>{{name}}</h1>
    <input type="text" v-model="name">
    <button @click="onClick">Trigger</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: "About me I'm awsome too"
    }
  },
  methods: {
    onClick() {
      alert(this.name)
    }
  }
}
</script>