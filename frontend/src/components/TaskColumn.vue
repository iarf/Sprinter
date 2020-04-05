<template lang="html">
  <b-col cols="12" md="4" class="task-col">
    <div class="col-wrapper">
      <h2 class="text-secondary">{{title}}</h2>
      <hr>
      <div class="droppable" v-on:drop="drop" v-on:dragover="allowDragging">
        <TaskCard v-for="task in tasks" :key="task.id" :name="task.name" :desc="task.description" :points="task.points" :id="task.id"/>
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
    drop(e){
      e.preventDefault()
      let data = e.dataTransfer.getData('text')
      console.log(data)
      e.target.appendChild(document.getElementById(data))
      console.log(data)
    },
    allowDragging(e){
      e.preventDefault()
    }
  }
}
</script>

<style lang="sass" scoped>
.col-wrapper
  margin: 0
  box-shadow: 0 0 10px -5px black
  padding: 8px
.task-col
  margin: 0
  padding: 6px
  height: calc(100vh - 60px)
  overflow-y: scroll
.add-task-link
  margin: 10px
  display: inline-block
</style>
