import java.util.Scanner;

public class CoffeeMachine {

    static int water = 400;
    static int milk = 540;
    static int beans = 120;
    static int cups = 9;
    static int money = 550;

    static Boolean exit = false;

    static Scanner scanner = new Scanner(System.in);

    enum Status {
        CHOOSING, BUYING, FILLING, TAKING, REMAINING, EXITING
    }

    static Status curStatus = Status.CHOOSING;

    public static void main(String[] args) {


        do {
            System.out.println(curStatus);
            System.out.print("Write action (buy, fill, take, remaining, exit): ");
            String action = scanner.next();
            switch (action) {
                case "buy":
                    curStatus = Status.BUYING;
                    System.out.println(curStatus);
                    buy();
                    break;
                case "fill":
                    curStatus = Status.FILLING;
                    System.out.println(curStatus);
                    fill();
                    break;
                case "take":
                    curStatus = Status.TAKING;
                    System.out.println(curStatus);
                    take();
                    break;
                case "remaining":
                    curStatus = Status.REMAINING;
                    System.out.println(curStatus);
                    remaining();
                    break;
                case "exit":
                    exit();
                    System.out.println(curStatus);
                    break;
            }
        } while (curStatus != Status.EXITING);


    }

    static void buy() {
        //System.out.println("buy() called");
        System.out.println();
        System.out.print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ");
        String choice = scanner.next();
        switch (choice) {
            case "1": {
                if (canMakeCoffee(250, 0, 16)) {
                    water -= 250;
                    beans -= 16;
                    cups--;
                    money += 4;
                }
		break;
            }
            case "2": {
                if (canMakeCoffee(350, 75, 20)) {
                    water -= 350;
                    milk -= 75;
                    beans -= 20;
                    cups--;
                    money += 7;
                }
		break;
            }
            case "3": {
                if (canMakeCoffee(200, 100, 12)) {
                    water -= 200;
                    milk -= 100;
                    beans -= 12;
                    cups--;
                    money += 6;
                }
		break;
            }
            case "back": {
                break;
            }
            default: {
                break;
            }

        }
        curStatus = Status.CHOOSING;
    }

    static void fill() {
        //System.out.println("fill() called");
        System.out.println();
        System.out.print("Write how many ml of water do you want to add: ");
        int waterAdd = scanner.nextInt();
        System.out.println();
        System.out.print("Write how many ml of milk do you want to add: ");
        int milkAdd = scanner.nextInt();
        System.out.println();
        System.out.print("Write how many grams of coffee beans do you want to add: ");
        int beansAdd = scanner.nextInt();
        System.out.println();
        System.out.print("Write how many disposable cups of coffee do you want to add: ");
        int cupsAdd = scanner.nextInt();
        System.out.println();
        water += waterAdd;
        milk += milkAdd;
        beans += beansAdd;
        cups += cupsAdd;

        curStatus = Status.CHOOSING;
    }

    static void take() {
        //System.out.println("take() called");
        System.out.println("I gave you $" + money +"\n");
        money = 0;

        curStatus = Status.CHOOSING;
    }

    static void remaining() {
        System.out.println();
        System.out.println("The coffee machine has:");
        System.out.println(water + " ml of water");
        System.out.println(milk + " ml of milk");
        System.out.println(beans + " grams of coffee beans");
        System.out.println(cups + " pieces of disposable cups");
        System.out.println(money + " dollars");
        System.out.println();

        curStatus = Status.CHOOSING;
    }

    static void exit() {
        //System.out.println("exit() called");
        curStatus = Status.EXITING;
    }

    static boolean canMakeCoffee(int waterNeed, int milkNeed, int beansNeed) {
        if (water >= waterNeed) {
            if (milk >= milkNeed) {
                if (beans >= beansNeed) {
                    System.out.println("The coffee is being ready!\n");
                    return true;
                } else {
                    System.out.println("Sorry, not enough beans!");
                    return false;
                }

            } else {
                System.out.println("Sorry, not enough milk!");
                return false;
            }
        } else {
            System.out.println("Sorry, not enough water!");
            return false;
        }
    }

}

