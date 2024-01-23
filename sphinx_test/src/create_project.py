import pulumi
import pulumi_azuredevops as azuredevops
import pulumi_github as github

class GitHubToAzureDevOpsProject:
    """
    Represents a project that integrates GitHub with Azure DevOps.

    Args:
        github_repo_name (str): The name of the GitHub repository.
        azure_project_name (str): The name of the Azure DevOps project.
        organization (str): The organization associated with the project.
    """

    def __init__(self, github_repo_name: str, azure_project_name: str, organization: str):
        self.github_repo_name = github_repo_name
        self.azure_project_name = azure_project_name
        self.organization = organization
        
        self.__create_project()
        self.__import_git_repo()
        self.__create_pipeline()

    def __create_project(self) -> None:
        """
        Creates a new Azure DevOps project with the specified settings.
        """
        self.project = azuredevops.Project("pipeline_vul1",
                description="Vulnerable pipeline 1",
                features={
                    "artifacts": "disabled",
                    "testplans": "disabled",
                },
                version_control="Git",
                visibility="private",
                work_item_template="Agile")

    def __import_git_repo(self) -> None:
        """
        Imports the specified GitHub repository into the Azure DevOps project.
        """
        initialization = azuredevops.GitInitializationArgs(
        init_type="Import",
        source_type="Git",
        source_url=self.github_repo_name,
        )

        self.git_repository = azuredevops.Git(
        "git_repository_vuln_1",
        name="pipeline_vul1",
        project_id=self.project.id,
        initialization=initialization
        )
    
    def __create_pipeline(self) -> None:
        """
        Creates a pipeline in the Azure DevOps project using the imported GitHub repository.
        """
        build_definition = azuredevops.BuildDefinition("BuildDefinition",
            project_id=self.project.id,
            ci_trigger=azuredevops.BuildDefinitionCiTriggerArgs(
                use_yaml=True,
                ),
            repository=azuredevops.BuildDefinitionRepositoryArgs(
                repo_type="TfsGit",
                repo_id=self.git_repository.id,
                yml_path="azure-pipelines.yml",
                ),
            variables=[
                azuredevops.BuildDefinitionVariableArgs(
                    name="SECRET",
                    is_secret=True,
                    secret_value="secret_value_btw",
                )
            ]
        )
    



        