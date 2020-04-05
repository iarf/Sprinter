<template lang="">
  <div class="task-card" draggable="true" v-on:dragstart="drag">
    <p class="task-title">{{name}}</p>
    <hr>
    <p class="task-desc text-secondary">{{desc}}</p>
    <p class="task-points text-muted">{{points}} pts</p>
  </div>
</template>

<script>
export default {
  props: [
    'name',
    'desc',
    'points',
  ],
  methods: {
    drag(e){
      e.dataTransfer.setData('text', e.target.id)
      console.log(this.$refs)
    },
    drop(e){
      e.preventDefault()
      let data = e.dataTransfer.getData('text')
      e.target.appendChild(document.getElementById('data'))
      console.log(data)
    }
  }
}
</script>

<style lang="sass">
  .task-card
    box-shadow: 0 0 10px -6px black
    padding: 6px
    margin-top: 10px
    position: relative
    hr
      width: 50%
    .task-desc
      padding-bottom: 20px
    .task-title
      font-weight: bold
      font-size: 1.25em
    .task-points
      display: inline-block
      position: absolute
      right: 10px
      bottom: -5px
      background: rgba(255,255,255,0.5)
</style>
