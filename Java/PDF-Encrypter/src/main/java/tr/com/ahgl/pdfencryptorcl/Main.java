package tr.com.ahgl.pdfencryptorcl;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.encryption.AccessPermission;
import org.apache.pdfbox.pdmodel.encryption.StandardProtectionPolicy;
import java.io.*;
import java.nio.file.Files;
public class Main{
    private static final int INVALID_PARAMETERS_EXIT_CODE = -3;
    private static final int ENCRYPTION_ERROR_EXIT_CODE = -5;
    private static final int TARGET_FILE_WRITE_ERROR_EXIT_CODE = -7;
    private static final int KEY_LENGTH = 128;
    public static void main(String[] args) {
        try {
            checkParameters(args);
        } catch (Exception e) {
            System.exit(INVALID_PARAMETERS_EXIT_CODE);
        }
        String password = args[0];
        File pdfToEncrypt = new File(args[1]);
        File encryptedPdfFile = new File(args[2]);
        byte[] encryptedPdfBytes = null;
        try {
            encryptedPdfBytes = encryptPdf(Files.readAllBytes(pdfToEncrypt.toPath()), password);
        } catch (IOException ex) {
            ex.printStackTrace();
            System.exit(ENCRYPTION_ERROR_EXIT_CODE);
        }
        try {
            writeBytesToFile(encryptedPdfFile, encryptedPdfBytes);
        } catch (IOException ex) {
            ex.printStackTrace();
            System.exit(TARGET_FILE_WRITE_ERROR_EXIT_CODE);
        }
    }
    private static void checkParameters(String[] args) throws Exception {
        if (args.length != 3) {
            System.out.println("-----------------------------------");
            System.out.println("Invalid parameters");
            System.out.println("Correct parameters: <password> <full path of pdf file> <full path of encrypted pdf file>");
            System.out.println("Example: \"123456\" \"/usr/dev/normal.pdf\" \"/usr/dev/encrypted.pdf\"");
            System.out.println("-----------------------------------");
            throw new Exception();
        }
    }
    private static byte[] encryptPdf(byte[] sourcePdfBytes, String password) throws IOException {
        PDDocument doc = PDDocument.load(sourcePdfBytes);
        AccessPermission ap = new AccessPermission();
        ap.setCanPrint(false);
        ap.setCanAssembleDocument(false);
        ap.setCanExtractContent(false);
        ap.setCanExtractForAccessibility(false);
        ap.setCanFillInForm(false);
        ap.setCanModify(false);
        ap.setCanModifyAnnotations(false);
        ap.setCanPrintDegraded(false);
        StandardProtectionPolicy spp = new StandardProtectionPolicy(
                password, password, ap);
        spp.setEncryptionKeyLength(KEY_LENGTH);
        doc.protect(spp);
        ByteArrayOutputStream baos = new ByteArrayOutputStream();
        doc.save(baos);
        doc.close();
        return baos.toByteArray();
    }
    private static void writeBytesToFile(File file, byte[] fileBytes) throws IOException {
        FileOutputStream faos = new FileOutputStream(file, false);
        faos.write(fileBytes);
        faos.close();
    }
}