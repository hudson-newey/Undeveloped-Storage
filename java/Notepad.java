import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Font;
import javax.swing.*;


class Notepad {
  public static void main(String[] args) {
    JFrame f = new JFrame("Notepad");
    f.setSize(600, 550);
    f.setLocation(300,200);
    final JTextArea textArea = new JTextArea(10, 40);
    f.getContentPane().add(BorderLayout.CENTER, textArea);
    textArea.setFont(new Font("Dialog", Font.PLAIN, 16));

    f.setVisible(true);
  }
}
