public class Main {

    public static void main(String[] args) {

        Customer customer = new Customer(101, "Rahul Sharma");

        FoodItem burger = new FoodItem("Burger", 150.0);
        FoodItem pizza  = new FoodItem("Pizza",  300.0);
        FoodItem coffee = new FoodItem("Coffee", 100.0);

        Order order = new Order(customer);

        order.addItem(burger);
        order.addItem(pizza);
        order.addItem(coffee);

        Discount discount = new PremiumCustomerDiscount();

        double totalBill      = order.calculateBill();
        double discountAmount = discount.calculateDiscount(totalBill);
        double finalBill      = totalBill - discountAmount;

        System.out.println("==============================");
        System.out.println("        ORDER SUMMARY         ");
        System.out.println("==============================");
        System.out.println();

        order.getCustomer().display();
        System.out.println();

        order.displayOrderedItems();
        System.out.println();

        System.out.println("Total Bill       : \u20b9" + totalBill);
        System.out.println("Discount Applied : \u20b9" + discountAmount);
        System.out.println("Final Bill       : \u20b9" + finalBill);
    }
}
