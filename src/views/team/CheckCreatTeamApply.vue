<template>
	<div>
		<sysManagerHomeHeader></sysManagerHomeHeader>
		<div class="apply-list">
			<el-table :data="teams" border height="600px">
				<el-table-column prop="name" label="团队名称" width="300px"></el-table-column>
				<el-table-column prop="time" label="申请时间" width="250px"></el-table-column>
				<el-table-column label="操作">
					<template slot-scope="scope">
						<el-button type="text" @click="viewTeam(scope.row.id)">查看详情</el-button>
						<el-button type="text" @click="dealApply(scope.row.id)">处理申请</el-button>
					</template>
				</el-table-column>
			</el-table>
		</div>
		<!--审核结果dialog-->
		<div>
			<el-dialog title="审核结果反馈" :visible.sync="resultDialogVisible">
				<el-form :model="form" label-width="80px">
					<el-form-item label="审核结果">
						<el-radio-group v-model="form.result">
							<el-radio label="通过"></el-radio>
							<el-radio label="拒绝"></el-radio>
						</el-radio-group>
					</el-form-item>
					<el-form-item label="原因">
						<el-input v-model="form.reason"></el-input>
					</el-form-item>
					<el-form-item>
						<div>
							<el-button @click="submitForm()">提交</el-button>
							<el-button @click="resultDialogVisible = flase">取消</el-button>
						</div>
					</el-form-item>
				</el-form>
			</el-dialog>
		</div>
	</div>
</template>

<script>
import sysManagerHomeHeader from "@/components/sysManagerHomeHeader/"
export default {
	components: {sysManagerHomeHeader},
	async created() {
		await this.axios({
			method: 'post',
			url: 'http://localhost:8000/buaa_db/admin_get_apply_team/',
			headers: {'Content-Type': 'multipart/form-data'},
		}).then((res)=>{
			this.teams = res.data.teams;
		})
	},
	data() {
		return {
			resultDialogVisible: false,
			form: {team_id:'', result: '', reason:''},
			teams : [
				{id:1, name:"团体一", time:"2023-10-18"},
				{id:2, name:"团体二", time:"2023-10-21"},
				{id:3, name:"团体一", time:"2023-10-18"},
				{id:4, name:"团体二", time:"2023-10-21"},
				{id:5, name:"团体一", time:"2023-10-18"},
				{id:6, name:"团体二", time:"2023-10-21"},
				{id:7, name:"团体一", time:"2023-10-18"},
				{id:8, name:"团体二", time:"2023-10-21"},
			]
		}
	},
	methods: {
		viewTeam(id) {
			this.$router.push({
				path: '/team/' + id
			})
		},
		dealApply(id) {
			this.form.team_id = id;
			this.resultDialogVisible = true; //sync
		},
		submitForm() {
			this.axios({
				method: 'post',
				url: 'http://localhost:8000/buaa_db/admin_check_apply_team/',
				headers: {'Content-Type': 'multipart/form-data'},
				data: this.form
			}).then((res)=>{
				if (res.data.status == 200) {
					this.$message({
						message: '审核提交成功',
						type: 'success'
					})
				}
				else {
					this.$message.error('审核提交失败')
				}
			})
		},
	}
}
</script>

<style scoped>
	.el-card {
		width: 100%;
	}
	.apply-list {
		margin: 20px 120px 0 120px;
	}
</style>