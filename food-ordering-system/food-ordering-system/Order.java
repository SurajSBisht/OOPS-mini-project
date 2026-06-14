public class Order {

    private Customer customer;
    private FoodItem[] items;
    private int itemCount;

    private static final int MAX_ITEMS = 5;

    public Order(Customer customer) {
        this.customer = customer;
        this.items = new FoodItem[MAX_ITEMS];
        this.itemCount = 0;
    }

    public void addItem(FoodItem item) {
        if (itemCount < MAX_ITEMS) {
            items[itemCount] = item;
            itemCount++;
        } else {
            System.out.println("Cannot add more than " + MAX_ITEMS + " items to an order.");
        }
    }

    public void displayOrderedItems() {
        System.out.println("Ordered Items");
        for (int i = 0; i < itemCount; i++) {
            items[i].display();
        }
    }

    public double calculateBill() {
        double total = 0;
        for (int i = 0; i < itemCount; i++) {
            total += items[i].getPrice();
        }
        return total;
    }

    public Customer getCustomer() {
        return customer;
    }
}
