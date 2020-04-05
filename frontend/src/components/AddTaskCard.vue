<template lang="html">
<div class="task-card">
  <i class="fas fa-times close-task link-secondary" v-on:click="closeTask"></i>
  <b-form action="index.html" method="post">
    <b-form-input
    name="title"
    class="task-input"
    placeholder="Name"/>
    <b-form-textarea
    name="description"
    class="task-input"
    placeholder="Description"/>
    <b-form-input
    name="points"
    label="pts:"
    class="task-input task-point-input"
    type="number"
    placeholder="pts"
    min="0"
    max="100"/>
    <b-button name="submit" type="submit" variant="success">Add</b-button>
  </b-form>
</div>
</template>

<script>
export default {
  methods: {
    closeTask(){
      this.$el.classList.toggle('hidden');
      this.$el.querySelector('form').reset();
    }
  }
}
</script>

<style lang="sass" scoped>
  .hidden
    display: none
  .close-task
    position: absolute
    top: 0
    right: 0
    padding: 5px
    cursor: pointer
  .task-card
    padding: 20px
    text-align: right
  .task-input
    margin-bottom: 10px
  .task-point-input
    width: 100px
    margin-right: 10px
    display: inline-block
</style>
