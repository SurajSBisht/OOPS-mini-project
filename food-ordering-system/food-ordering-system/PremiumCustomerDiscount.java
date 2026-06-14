public class PremiumCustomerDiscount extends Discount {

    @Override
    public double calculateDiscount(double amount) {
        return amount * 0.15;
    }
}
