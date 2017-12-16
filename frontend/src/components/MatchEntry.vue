<template>
  <div class="Package">
    <h1 class="Package__title">{{ name }}</h1>
    <router-link :to="{ name: 'match', params: { 'id': id, 'region': shard }}">{{ name }}</router-link>
    <div class="Package__info">
      <div class="Package__info-item">
        <span>{{ id }}</span><span class="info-label">ID</span>
      </div>
      <div class="Package__info-item">
        <span>{{ shard }}</span><span class="info-label">Region</span>
      </div>
    </div>
  </div>


</template>

<script>
  export default {
    props: {
      name: {
        type: String
      },
      id: {
        type: String
      },
      shard: {
        type: String
      }
    }
  }
</script>
