import java.util.*;

public class Main {

  public static void main(String[] args) {
    // The main method is the entry point of the program.
    // It calls the player_move function and passes its result to the com_move function.
    
    // Call player_move and store the result in the "something" variable
    String something = player_move();

    // Call com_move and pass the "something" variable as an argument
    com_move(something);
  }

  public static String player_move() {
    // The player_move method prompts the user to enter their move (rock, paper, or scissors).
    // It reads the input from the keyboard and returns the entered value.
    
    // Create a Scanner object to read input from the keyboard
    Scanner keyboard = new Scanner(System.in);

    // Prompt the user to choose rock, paper, or scissors
    System.out.println("Choose rock, paper, or scissors: ");

    // Read the user's input
    String option = keyboard.nextLine();

    // Return the user's input
    return option;
  }

  public static void com_move(String option) {
    // The com_move method takes the player's move as an argument and simulates the computer's move.
    // It compares the player's move with a randomly generated move by the computer and determines the winner.
    
    if (option.equals("rock")) {
      // If the player's move is "rock", the computer randomly chooses between "paper" and "scissors".

      String[] rock = {"paper", "scissors"};

      // Generate a random index to select an element from the rock array
      int comchoice1 = new Random().nextInt(rock.length); 

      // Get the computer's move based on the random index
      String rock1 = rock[comchoice1];

      // Print the computer's move
      System.out.println("Computer chooses: " + rock1);

      if (rock1.equals("scissors")) {
        // If the computer's move is "scissors", the player wins
        System.out.println("You win!");
      } else {
        // Otherwise, the computer wins