# -- FILE: features/branches.feature
Feature: Branches Service

  Scenario: Run a CreateBranch test
    Given a csv file "../data/properties_clean.csv" with a list of 28 properties
    When connected to a local branches grpc server at "localhost:9090"
    When posted the list to the branches service
    Then the service returns 6 responses with a success code
    When queried for the 3 branches list
    Then service returns a list of 6 unique branches to the client
