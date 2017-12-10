
<template>
  <div>
    <p>Home page</p>
    <p> {{ player }}</p>
    <button @click="getPlayer">New player</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      player: 0
    }
  },
  methods: {
    getPlayer () {
      const path = '/api/v1/players/eu/Shiqan'
      axios.get(path)
      .then(response => {
        console.log(response)
        this.player = response.data.data[0].id
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  created () {
    this.getPlayer()
  }
}
</script>
