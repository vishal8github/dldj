import java.security.spec.*;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import javax.crypto.SecretKey;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;

public class GeneratePublicPrivateKey{
    public static void generateKey(String keyAlgorithm, int numBits) throws NoSuchAlgorithmException, InvalidKeySpecException{
        KeyPairGenerator keygen = KeyPairGenerator.getInstance(keyAlgorithm);
        keygen.initialize(numBits);

        System.out.println("\nFor Algorithm: " + keyAlgorithm);
        KeyPair keypair = keygen.generateKeyPair();


        PrivateKey privateKey1 = keypair.getPrivate();

        PublicKey publicKey1 = keypair.getPublic();

        byte[] private1 = privateKey1.getEncoded();
        byte[] public1 = publicKey1.getEncoded();

        String privateFormat = privateKey1.getFormat();
        String publicFormat = publicKey1.getFormat();

        System.out.println("Private format: " + privateFormat + "\nPublic format: " + publicFormat);

        KeyFactory keyfactory = KeyFactory.getInstance(keyAlgorithm);

        EncodedKeySpec privateKeySpec = new PKCS8EncodedKeySpec(private1);


        PrivateKey privateKey2 = keyfactory.generatePrivate(privateKeySpec);

        EncodedKeySpec publicKeySpec = new X509EncodedKeySpec(public1);

        PublicKey publicKey2 = keyfactory.generatePublic(publicKeySpec);


        System.out.println("Are both private keys equal? " + privateKey1.equals(privateKey2));

        System.out.println("Are both public keys equal? " + publicKey1.equals(publicKey2));

        System.out.println("Are private key1 and public key1 equal? " + privateKey1.equals(publicKey1));

        System.out.println("Are private key2 and public key2 equal? " + privateKey2.equals(publicKey2));
    }

    public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeySpecException{
        generateKey("RSA", 1024);
        generateKey("DSA", 1024);
        generateKey("DH", 1024);
    }
}
