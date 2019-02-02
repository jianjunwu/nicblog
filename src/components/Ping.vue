<template>
  <div>
    <p> {{ msg }} </p>
    <button type="button" class="btn btn-primary"> {{msg}} </button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Ping',
  data () {
    return {
      msg: 'Hello, This is Ping.vue component'
    }
  },
  methods: {
    getMessage () {
      const url = 'http://127.0.0.1:5000/ping'
      axios.get(url)
        .then((res) => {
          this.msg = res.data
        })
        .catch((error) => {
          console.error(error)
        })
    }
  },
  created () {
    this.getMessage()
  }
}
</script>
