<template>
  <div id="app">

    <form @submit.prevent="submitForm" action="">
      <div class="form-group row">
        <input type="text" placeholder="Name" class="form-control col-3 mx-2" v-model="student.Name">
        <input type="text" placeholder="Course" class="form-control col-3 mx-2" v-model="student.Course">
        <input type="text" placeholder="Rating" class="form-control col-3 mx-2" v-model="student.Rating">
        <button class="btn btn-success">Submit</button>
      </div>
    </form>

    <table class="table">
      <thead>
        <th>Name</th>
        <th>Course</th>
        <th>Rating</th>
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.id" @dblclick="$data.student = student">
          <td>{{student.Name}}</td>
          <td>{{student.Course}}</td>
          <td>{{student.Rating}}</td>
          <td class="btn btn-outline-danger btn-sm mx-1" @click="deleteStudent(student)">X</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'App',
  data(){
    return {
      student: {
        'Name':'',
        'Course':'',
        'Rating':''        
      },
     students: []
    }
  },
  async created(){
   await this.getStudent();
  },

  methods:{
    
    submitForm(){
      if(this.student.id === undefined){
        this.createStudent();
      }else{
        this.editStudent();
      }
    },

    async getStudent(){
      var response = await fetch('http://localhost:8000/api/students/');
      this.students = await response.json();
    },

    async createStudent(){
      this.getStudent();
      await fetch('http://localhost:8000/api/students/',{
        method: 'post',
        headers:{
          'Content-Type': 'application/json'
        },
        body:JSON.stringify(this.student)
      });
      this.getStudent();
      this.student = {}
    },

    async editStudent(){
      this.getStudent();
      await fetch(`http://localhost:8000/api/students/${this.student.id}/`,{
        method: 'put',
        headers:{
          'Content-Type': 'application/json'
        },
        body:JSON.stringify(this.student)
      });
      this.getStudent();
      this.student = {}
    },
    async deleteStudent(student){
      this.getStudent();
      await fetch(`http://localhost:8000/api/students/${student.id}/`,{
        method: 'delete',
        headers:{
          'Content-Type': 'application/json'
        },
        body:JSON.stringify(this.student)
      });
      this.getStudent();
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
