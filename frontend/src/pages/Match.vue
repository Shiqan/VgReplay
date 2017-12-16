<template>
  <div class="content">
    <div class="container">
      <div class="error-message" v-if="showError">
       {{ errorMessage }}
      </div>
      {{ id }} - {{ shard }}
      <hr>
      <telemetry-event v-bind:televent="televent" v-if="loaded" v-for="televent in eventList" :key="televent.time"></telemetry-event>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import TelemetryEvent from '@/components/TelemetryEvent'
  import { dateToDay } from '../utils/dateFormatter'

  export default {
    components: {
      TelemetryEvent
    },
    metaInfo () {
      return {
        title: this.name ? `${this.name} | 📈 Search Player(s)` : '📈 Player(s) searched',
        meta: [
          { vmid: 'description', name: 'description', content: 'stuff' }
        ]
      }
    },

    data () {
      return {
        loaded: false,
        loading: false,
        id: '',
        shard: '',
        showError: false,
        showSettings: false,
        errorMessage: 'Please enter player name(s)',
        periodStart: '',
        periodEnd: new Date(),
        eventList: []
      }
    },

    mounted () {
      if (this.$route.params.id) {
        this.shard = this.$route.params.region
        this.id = this.$route.params.id
        this.requestData()
      }
    },

    computed: {
      metaHeadTitle () {
        return this.name
          ? `📈 Flue ${this.name}`
          : `📈 Flue`
      },
      _endDate () {
        return dateToDay(this.periodEnd)
      },
      _startDate () {
        return dateToDay(this.periodStart)
      }
    },

    methods: {
      resetState () {
        this.loaded = false
        this.showError = false
      },
      requestData () {
        if (this.id === null || this.id === '' || this.id === 'undefined') {
          this.showError = true
          return
        }
        this.resetState()
        this.loading = true
        axios.get(`http://localhost:8080/api/v1/telemetry/${this.shard}/${this.id}`)
          .then(response => {
            console.log(response)
            this.eventList = response.data

            this.loaded = true
            this.loading = false
          })
          .catch(err => {
            console.log(err)
            this.errorMessage = err.response.data.errors.map(entry => entry.title)
            this.showError = true
          })
      },
      validateDataRequest () {
        console.log('ValidateData')
        if (this.name !== '' && this.periodStart !== '') {
          this.requestData()
        }
      },
      toggleSettings () {
        this.showSettings = !this.showSettings
      }
    }
  }
</script>
