<template>
  <div class="Package">
    <h1 class="Package__title">{{ televent.time }}</h1>
    <div class="Package__info">
      <div class="Package__info-item">
        <span>{{ televent.type }}</span><span class="info-label"> {{ televent.payload.Hero }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['televent']
}
</script>
