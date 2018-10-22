from MessageFormer import MessageFormer
from FileReader import FileReader

class MessagesFormer():
    def FormAllMessages(self, ebookTitle):
        messageFormer = MessageFormer()
        addressees = self.GetAddressees()
        messages = []
        senderAddress = self.GetSenderAddress()

        for address in addressees:
            newMessage = messageFormer.FormMessage(ebookTitle, senderAddress, address)
            messages.append(newMessage)
        return messages

    def GetAddressees(self):
        fileReader = FileReader()
        addressees = fileReader.ReadLines("addressees.txt")
        return addressees

    def GetSenderAddress(self):
        fileReader = FileReader()
        address = fileReader.ReadOneLine("senderAddress.txt")
        return address