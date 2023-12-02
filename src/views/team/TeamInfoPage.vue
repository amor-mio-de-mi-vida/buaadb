<template>
	<div>
		<div>
			<homeHeader></homeHeader>
		</div>
		<div class="content">
			<div class="team-description">
				<el-descriptions title="团体信息" column="1">
					<el-descriptions-item label="团体名称">{{team_name}}</el-descriptions-item>
					<el-descriptions-item label="团体简介">{{description}}</el-descriptions-item>
				</el-descriptions>
			</div>
			<!--div>
				<el-button @click="request_join()">申请加入团体</el-button>
				<el-button @click="request_quit()">申请退出团体</el-button>
			</div-->
			<el-divider></el-divider>
			<div class="team-project">
				<div class="team-project-title">发起的项目</div>
				<div class="project">
					<el-table :data="projects" stripe :header-cell-style="{background:'#E4E7ED',color:'#303133'}">
						<el-table-column prop="project_name" label="项目名称"></el-table-column>
						<el-table-column prop="position" label="地点"></el-table-column>
						<el-table-column prop="time" label="日期"></el-table-column>
						<el-table-column label="操作">
							<template slot-scope="scope">
								<el-button type="text" @click="viewProject(scope.row.id)">查看详情</el-button>
							</template>
						</el-table-column>
					</el-table>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import homeHeader from "@/components/homeHeader";
	export default {
		components: {homeHeader},
		data() {
			return {
				id: '1',
				team_name: '团体1',
				description: '这是一个团体balabala',
				projects : [
					{id:1, project_name:"活动一",position:"操场", time:"2023-10-18", description: "", status: ""},
					{id:2, project_name:"活动二",position:"主楼", time:"2023-10-21", description: "", status: ""},
					{id:3, project_name:"活动一",position:"操场", time:"2023-10-18", description: "", status: ""},
					{id:4, project_name:"活动二",position:"主楼", time:"2023-10-21", description: "", status: ""},
					{id:5, project_name:"活动一",position:"操场", time:"2023-10-18", description: "", status: ""},
					{id:6, project_name:"活动二",position:"主楼", time:"2023-10-21", description: "", status: ""},
					{id:7, project_name:"活动二",position:"主楼", time:"2023-10-21", description: "", status: ""},
				],
				image_id: '',
				image_url: '',
				image_post_time: '',
				students: [
					{id: '', name: ''}
				],
				managers: [
					{id: '', name: ''}
				]
			}
		},
		async created(){
			await this.axios({
				method: 'post',
				url: 'http://localhost:8000/buaa_db/get_team_profile/',
				headers: {'Content-Type': 'multipart/form-data'},
				data: {
					'team_id': this.$route.params.id
				}
			}).then((res) => {
				this.team_name = res.data.name
				this.description = res.data.profile
				this.image_id = res.data.image_id
				this.image_url = res.data.image_url
				this.image_post_time = res.data.image_post_time
				this.projects = res.data.projects
				this.students = res.data.students
				this.managers = res.data.managers
			})
			await this.axios({
				method: 'post',
				url: 'http://localhost:8000/buaa_db/get_team_projects/',
				headers: {'Content-Type': 'multipart/form-data'},
				data: {
					'team_id': this.$route.params.id
				}
			}).then((res)=>{
				this.projects = res.data.projects
			})
		},
		methods: {
			viewProject(id) {
				this.$router.push('/project/' + id);
			}
		}
	}
</script>

<style scoped>
	.team-project-title {
		margin-bottom: 20px;
		font-size: larger;
		font-weight:500;
	}
	.image {
	width: 100%;
	height: 150px;
	display: block;
	background-size: cover;
	background-position: center center;
	}
	.box-card {
		width: 480px;
	}
	.card-context {
		margin: 10px 20px 10px 20px;
		line-height: 25px;
	}
	.el-row {
		display:flex;
		flex-wrap: wrap;
		align-items: center;
	}
	.el-row  .el-card {
		width: 100%;
		height: 100%;
		margin-right: 20px;
		margin-bottom: 30px;
		transition: all .5s;
	}
	.el-table{
		margin-left: 10px;
		margin-right: 10px;
		border: 1px solid #ccc;
	}
	.el-descriptions {
		font-size: medium;
	}
</style>