<template lang="">
  <div class="task-card" draggable="true" v-on:dragstart="drag" :task-id="this.$vnode.key">
    <p class="task-title">{{name}}</p>
    <hr>
    <p class="task-desc text-secondary">{{desc}}</p>
    <p class="task-points text-muted">{{points}} pts {{this.$vnode.key}}</p>
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
      e.dataTransfer.setData('text',e.target.getAttribute('task-id'))
    },
    dragEnd(){
      let dragOvers = document.querySelectorAll('.drag-over')
      for (let i = 0; i < dragOvers.length; i++){
        dragOvers[i].classList.remove('drag-over')
      }
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
    background: white
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
