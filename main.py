import Project

if __name__ == '__main__':
    project = Project.ProjectContainer()
    project.clear_repos_folder()
    project.clone_repos()
    project.create_repos()
    project.process_repos()
    project.display_info()


