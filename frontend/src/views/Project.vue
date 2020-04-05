<template lang="html">
  <div class="">
    <ProjectNavBar :name="project.name"/>
    <ProjectTeam id="team-menu"/>
    <ProjectTasks id="tasks-window" :tasks="project.tasks"/>
  </div>
</template>

<script>
import ProjectTasks from '../components/ProjectTasks.vue'
import ProjectNavBar from '../components/ProjectNavBar.vue'
import ProjectTeam from '../components/ProjectTeam.vue'
import axios from 'axios'

export default {
  name: 'Project',
  data(){
    return{
      project: [],
      tasks: [],
    }
  },
  components:{
    ProjectTasks,
    ProjectNavBar,
    ProjectTeam
  },
  methods: {
    getProjectDetails(){
      axios
        .get('http://127.0.0.1:8000/api/projects/2/')
        .then(response => (this.project = response.data))
        .catch(error => (console.log(error)));

      axios
        .get('http://127.0.0.1:8000/api/tasks/2/')
        .then(response => (this.tasks = response.data))
        .catch(error => (console.log(error)));
    }
  },
  created(){
    this.getProjectDetails()
  }
}
</script>

<style lang="sass" scoped>
  #tasks-window
    transition: .3s ease-in-out

    &.show-team
      margin-right: 220px
</style>
