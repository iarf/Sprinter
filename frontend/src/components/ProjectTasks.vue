<template lang="html">
  <div class="task-window">
    <b-container fluid>
      <b-row>
        <TaskColumn title="To-do" :tasks="toDo"></TaskColumn>
        <TaskColumn title="In Progress" :tasks="inProgress"></TaskColumn>
        <TaskColumn title="Done" :tasks="done"></TaskColumn>
      </b-row>
    </b-container>
  </div>
</template>

<script>
  import TaskColumn from './TaskColumn.vue'

  export default {
    components: {
      TaskColumn
    },
    props: {
      tasks: {
        type: Array,
        default: function(){
          return []
        }
      }
    },
    computed: {
      toDo(){
        return this.tasks.filter(task => {return task.status == 1})
      },
      inProgress(){
        return this.tasks.filter(task => {return task.status == 2})
      },
      done(){
        return this.tasks.filter(task => {return task.status == 3})
      }
    }
  }
</script>

<style lang="sass" scoped>
  .task-window
    height: 100vh
    z-index: 0
    position: absolute
    top: 0
    padding-top: 60px

</style>
