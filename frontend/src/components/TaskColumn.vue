<template lang="html">
  <b-col cols="12" md="4" class="task-col">
    <div class="col-wrapper">
      <h2 class="text-secondary">{{title}}</h2>
      <hr>
      <div class="droppable" v-on:dragover="dragAllow" v-on:drop="drop" v-on:dragleave="dragLeave">
        <TaskCard v-for="task in tasks" :key="task.id" :name="task.name" :desc="task.description" :points="task.points"/>
        <AddTaskCard />
      </div>
      <a href="#" class="add-task-link">Add Task</a>
    </div>
  </b-col>

</template>

<script>
import AddTaskCard from './AddTaskCard.vue'
import TaskCard from './TaskCard.vue'

export default {
  components: {
    AddTaskCard,
    TaskCard
  },
  props: [
    'title',
    'tasks'
  ],
  methods: {
    dragAllow(e){
      if (e.target.classList.contains('droppable')){
        e.preventDefault()
        e.target.classList.add('drag-over')
      }
    },
    drop(e){
      e.preventDefault()
      let data = e.dataTransfer.getData('text')
      console.log(data)
      e.target.classList.remove('drag-over')
    },
    dragLeave(e){
      e.target.classList.remove('drag-over')
    }
  }
}
</script>

<style lang="sass" scoped>
.col-wrapper
  margin: 0
  box-shadow: 0 0 10px -5px black
  padding: 0
.task-col
  margin: 0
  padding: 6px
  height: calc(100vh - 60px)
  overflow-y: scroll
.add-task-link
  margin: 10px
  display: inline-block
.droppable
  padding: 8px
  padding-bottom: 60px
  *
    transition: all .2s ease-in-out
.drag-over
  background: #a3bcc9
  *
    transform: scale(.8)
    transition: all .2s ease-in-out
</style>
