# Module 5: Push the docker container to Amazon ECR 

Amazon Elastic Container Registry (ECR) is a fully-managed Docker container registry that makes it easy for developers to store, manage, and deploy Docker container images. 

## Instructions
1. Go to the [ECR Console](https://ap-southeast-1.console.aws.amazon.com/ecs/home?region=ap-southeast-1#/repositories) (You can reach there also by looking for "ECS" or "container service" in the list of services from the console home page and go to ECR **Repositories** 
	
1. Click on **Create repository**

1. Give a name, such as `<your-username>-aws-batch-workshop` to your repo, then click **Next Step**

	<img src="images/create-ecr-repo.png"  width="90%"/>
	
1. As you go to your repository, and click `View push commands` as the following screen, you will be presented many useful commands. 

	![](images/ecr-commands.png)	

	Follow the commands (1-4) to login to the registry, build the container, tag the container and push to the repo.
	
1. After the push succeeds, now if you check your ECR repository, you should see the pushed docker image

	<img src="images/check-ecr-image.png" width="90%" />
	
## Next step

Move on to [**Module 6: Create an IAM role for the container**](./Module6.md)
