<template lang="html">
  <div class="team-menu collapsed">
    
  </div>
</template>

<script>
export default {
}
</script>

<style lang="sass" scoped>
  .team-menu
    width: 220px
    height: 100vh
    position: fixed
    right: 0
    top: 0
    background: white
    box-shadow: 0 0 10px -5px black
    transition: all .3s ease-in-out

    &.collapsed
      width: 0
      transition: all .3s ease-in-out
</style>
